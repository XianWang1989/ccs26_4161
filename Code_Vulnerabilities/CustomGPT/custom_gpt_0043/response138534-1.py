
from flask import Flask, redirect, url_for, flash
import json

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

    # Flash a message if needed
    flash("Elastic IP deleted successfully.", "success")

    # Redirect back to the page where the delete button was
    return redirect(url_for('your_display_route', region=region))

# Example route to display the page with Elastic IPs
@app.route('/elastic_ips/<region>')
def your_display_route(region):
    # Logic to render the page with Elastic IPs
    return "Here you would render your Elastic IPs for region: {}".format(region)

if __name__ == '__main__':
    app.run(debug=True)
