
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

    # Show a flash message after deletion if desired
    flash('Elastic IP deleted successfully.')

    # Redirect back to the list of elastic IPs or another appropriate route
    return redirect(url_for('your_elastic_ip_list_route', region=region))

@app.route('/elastic_ips/<region>')
def your_elastic_ip_list_route(region):
    # Your code to render the list of elastic IPs
    return render_template('elastic_ips.html', region=region)
