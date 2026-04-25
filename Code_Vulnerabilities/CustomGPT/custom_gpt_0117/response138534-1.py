
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

    success = False
    for eli in elis:
        result = eli.release()
        success = True  # Set success to True if at least one IP is deleted

    if success:
        flash('Elastic IP deleted successfully.', 'success')
    else:
        flash('Failed to delete Elastic IP.', 'error')

    return redirect(url_for('your_redirect_function', region=region))

@app.route('/elastic_ips/<region>')
def your_redirect_function(region):
    # Render your page displaying the Elastic IPs
    # This could be a template that lists all IPs
    return render_template('elastic_ips.html', region=region)
