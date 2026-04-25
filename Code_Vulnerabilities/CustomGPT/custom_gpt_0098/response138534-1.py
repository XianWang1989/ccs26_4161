
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()

    # Flash a success message
    flash(f'Elastic IP {ip} has been deleted successfully.', 'success')

    # Redirect back to the page where the delete button is
    return redirect(url_for('your_page_function', region=region))

# Your page route (where the delete button is)
@app.route('/elastic_ips/<region>')
def your_page_function(region):
    # Logic to display the page goes here
    return render_template('your_template.html', region=region)
