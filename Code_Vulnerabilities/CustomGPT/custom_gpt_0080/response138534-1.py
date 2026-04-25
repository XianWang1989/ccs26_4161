
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

# Configure necessary settings for flash messages
app.secret_key = 'your_secret_key'

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

    # Optionally flash a message to inform the user of success/failure
    flash('Elastic IP deleted successfully!')

    # Redirect back to the desired page (e.g., a list of elastic IPs)
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to list elastic IPs for the specific region
    return render_template('elastic_ips_list.html', region=region)
