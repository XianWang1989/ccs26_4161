
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    try:
        elis = conn.get_all_addresses(addresses=ip)
        for eli in elis:
            eli.release()
        flash('Elastic IP deleted successfully.', 'success')
    except Exception as e:
        flash(f'Error deleting Elastic IP: {str(e)}', 'error')

    # Redirect back to the page displaying the elastic IPs
    return redirect(url_for('view_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def view_elastic_ips(region):
    # Logic to fetch and display Elastic IPs
    return render_template('elastic_ips.html', region=region)  # or however you are handling this
