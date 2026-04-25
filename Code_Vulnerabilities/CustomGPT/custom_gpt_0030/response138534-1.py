
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Attempt to delete the IP
    for eli in elis:
        r = eli.release()  # Assume this returns a result
        # Handle success or error messages
        flash(f'Successfully deleted IP: {ip.decode("ascii")}', 'success')

    # Redirect back to the list view or the previous page
    return redirect(url_for('your_list_view_route', region=region))

@app.route('/elastic_ips/<region>')
def your_list_view_route(region):
    # Your code to display the list of IPs
    pass
