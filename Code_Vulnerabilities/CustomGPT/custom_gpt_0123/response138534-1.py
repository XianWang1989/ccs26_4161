
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>', methods=['POST'])
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()

    # Flash a message to inform about the successful deletion
    flash('Elastic IP deleted successfully.')

    # Redirect back to the appropriate page
    return redirect(url_for('display_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def display_elastic_ips(region):
    # Your logic to display the elastic IPs
    return "Displaying Elastic IPs for region: {}".format(region)
