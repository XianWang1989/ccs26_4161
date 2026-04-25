
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

# Configuration for flash messages (remember to set a secret key)
app.secret_key = 'your_secret_key'

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Process the deletion
    try:
        for eli in elis:
            r = eli.release()
        # Flash a success message (optional)
        flash(f'Successfully deleted Elastic IP: {ip}')
    except Exception as e:
        # Flash an error message if something goes wrong (optional)
        flash(f'Error deleting Elastic IP: {str(e)}')

    # Redirect back to the page where the delete button is
    return redirect(url_for('your_target_route', region=region))

@app.route('/elastic_ips/<region>')
def your_target_route(region):
    # Your code to list Elastic IPs or the relevant view
    return render_template('your_template.html', region=region)
