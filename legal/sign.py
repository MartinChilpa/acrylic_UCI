import io
from dropbox_sign import ApiClient, ApiException, Configuration, apis, models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from catalog.models import Track
import weasyprint

configuration = Configuration(username=settings.DROPBOX_SIGN_API_KEY)


def send_signature_request_for_ownership_validation(track_id):

    track = get_object_or_404(Track, id=track_id)

    with ApiClient(configuration) as api_client:
        signature_request_api = apis.SignatureRequestApi(api_client)
        #signature_request_id = ''
        signers = []
        
        # add signers
        for split in track.master_splits.all():
            signer = models.SubSignatureRequestSigner(
                email_address=split.owner_email,
                name=split.owner_name,
            )
            signers.append(signer)

        # configure options
        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=False,
            default_type='draw',
        )

        # document in PDF format
        html_string = render_to_string('legal/split_sheet_pdf.html', {'track': track})
        pdf_file = weasyprint.HTML(string=html_string).write_pdf()
        
        import tempfile
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pdf') as temp_file:
            temp_file.write(pdf_file)
            temp_file.flush()

            #pdf_io = io.BytesIO(pdf_file)
            #pdf_io.seek(0)  # Go to the beginning of the "file"
            #pdf_content = pdf_io.read() 

            data = models.SignatureRequestSendRequest(
                title=f'Validate Ownership for {track.name}',
                subject=f'Validate Ownership for {track.name}',
                message=f"""
                    Please validate your ownership in the master of track "{track.name}" (ISRC: {track.isrc}) by {track.artist.name}. 

                    Click on the link below to validate your ownership.

                    Track information:
                    - ISRC: {track.isrc}
                    - Name: {track.name}
                    - Artist: {track.artist.name}
                    
                    Best,
                    Acrylic.LA
                """,
                signers=signers,
                cc_email_addresses=[
                    "antonio@acrylic.la",
                ],
                files=[open(temp_file.name,  "rb")],
                metadata={
                    "isrc": track.isrc,
                },
                signing_options=signing_options,
                test_mode=True,
            )
                
            
            try:
                response = response = signature_request_api.signature_request_send(data)
                # save signature
                track.signature_request_id = response.signature_request_id
                track.save()
                
            except ApiException as e:
                print("Exception when calling Dropbox Sign API: %s\n" % e)

    
    
        
