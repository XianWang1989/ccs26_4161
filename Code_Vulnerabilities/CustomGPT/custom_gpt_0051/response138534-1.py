
from flask import Flask, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

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

    if result:
        flash('Elastic IP deleted successfully.')
    else:
        flash('No Elastic IP found to delete.')

    return redirect(url_for('elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips(region):
    # Render your template or return the list of Elastic IPs
    return render_template('elastic_ips.html', region=region)

# Your HTML for the delete button
# <a href="{{ url_for('delete_elastic_ip', region=region, ip=eli['public_ip']) }}">
#     <button class="btn btn-danger btn-mini" type="button">Delete</button>
# </a>
