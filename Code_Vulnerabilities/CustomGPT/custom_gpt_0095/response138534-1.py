
from flask import Flask, redirect, url_for, flash, Response
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a success message (optional)
    flash('Elastic IP deleted successfully!')

    # Redirect to a desired route after deletion
    return redirect(url_for('show_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def show_elastic_ips(region):
    # Logic to display the list of elastic IPs
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
