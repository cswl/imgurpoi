import click

from imgurpoi import *

@click.command()
@click.argument("image", type=click.Path(exists=True))
def upload_image(image):
    config = get_config()
    if not config:
        click.echo(
            "Cannot upload - could not find IMGUR_API_ID or " "IMGUR_API_SECRET environment variables or config file"
        )
        return
    
    click.echo("Uploading file {}".format(click.format_filename(image)))
    imgur_resp= imgur_uploader(image, id=config["id"], secret=config["secret"])
    if imgur_resp["success"] == True :
        imgur_data = imgur_resp["data"]
        print (imgur_data.get("link"))
        print (imgur_data.get("deletehash"))
        
        try:
            import pyperclip
    
            pyperclip.copy(imgur_data["link"])
        except ImportError:
            print("pyperclip not found. To enable clipboard functionality," " please install it.")

if __name__ == "__main__":
    upload_image()