
from flask import Flask, redirect, url_for, request
import json

app = Flask(__name__)

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

    # Optionally, you can flash a message to inform the user about the delete action
    flash('Elastic IP deleted successfully!')  # Note: Ensure you set up sessions and flash messaging

    # Redirect back to the page that shows the list of Elastic IPs
    return redirect(url_for('elastic_ips_list', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips_list(region):
    # Your logic to display the list of Elastic IPs
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
