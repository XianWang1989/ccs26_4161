
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        result = []
        r = eli.release()
        result.append(r)

    # Flash a success message
    flash(f'Successfully deleted IP {ip}.')

    # Redirect back to the page with the delete button
    return redirect(url_for('your_view_function', region=region))  # Replace 'your_view_function' with the actual endpoint name

@app.route('/elastic_ips/<region>')
def your_view_function(region):
    # Render your page to display the IPs and the delete button
    return render_template('your_template.html', region=region)  # Replace with your actual template
