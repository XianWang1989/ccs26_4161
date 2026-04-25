
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'],
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Delete the IP
    for eli in elis:
        r = eli.release()

    # Flash a message for feedback (optional)
    flash(f'Successfully deleted IP: {ip}')

    # Redirect back to the page with the delete button
    return redirect(url_for('your_view_function', region=region))

@app.route('/elastic_ips/<region>')
def your_view_function(region):
    # Render your page with the delete button here
    return render_template('your_template.html', region=region)
