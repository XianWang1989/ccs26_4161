
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optionally, you might want to flash a message to inform the user
    flash(f'Successfully deleted elastic IP: {ip.decode()}')

    # After processing, redirect back to the page where the delete button was
    return redirect(url_for('your_view_function_name', region=region))

# Replace 'your_view_function_name' with the actual name of the route function
@app.route('/elastic_ips/<region>')
def your_view_function_name(region):
    # Logic to render the elastic IPs for the given region
    pass
