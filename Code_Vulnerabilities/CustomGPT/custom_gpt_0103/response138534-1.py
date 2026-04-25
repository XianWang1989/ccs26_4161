
from flask import Flask, redirect, url_for, request

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
        r = eli.release()  # Assuming this returns a result
        # You may want to handle or log the result as needed

    # Redirect back to the main page or another route after deletion
    return redirect(url_for('your_main_route', region=region))

@app.route('/elastic_ips/<region>')
def your_main_route(region):
    # Logic to display your elastic IPs
    return render_template('your_template.html', region=region)
