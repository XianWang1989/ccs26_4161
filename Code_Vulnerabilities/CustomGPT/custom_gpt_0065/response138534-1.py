
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()

    # Flash a message to inform the user about the operation
    flash(f'Successfully deleted Elastic IP: {ip.decode()}')

    # Redirect back to the list of Elastic IPs or a relevant page
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # This would return the Elastic IPs list page
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
