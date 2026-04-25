
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'],
                              aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip_encoded = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip_encoded)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message to indicate success or failure
    flash(f'Elastic IP {ip} has been deleted successfully.', 'success')

    # Redirect back to the list of Elastic IPs or the desired page
    return redirect(url_for('your_view_function_name', region=region))  # Replace with your actual view function name
