
from flask import Flask, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip_encoded = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip_encoded)

    result = []

    for eli in elis:
        r = eli.release()
        result.append(r)

    flash('Elastic IP deleted successfully!', 'success')  # Flash a success message
    return redirect(url_for('your_view_function', region=region))  # Redirect back to the view

@app.route('/elastic_ips/<region>')
def your_view_function(region):
    # Render your page with delete button here
    return "Your Elastic IP management page"

if __name__ == '__main__':
    app.run()
