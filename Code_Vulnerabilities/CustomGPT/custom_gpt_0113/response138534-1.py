
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

    # Attempt to release the IP
    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message (optional)
    flash(f'Successfully deleted IP: {ip.decode("ascii")}', 'success')

    # Redirect back to the main page (or wherever the delete button is)
    return redirect(url_for('your_main_route', region=region))

@app.route('/your_main_route/<region>')
def your_main_route(region):
    # Your logic here to render the main page
    return render_template('your_template.html', region=region)
