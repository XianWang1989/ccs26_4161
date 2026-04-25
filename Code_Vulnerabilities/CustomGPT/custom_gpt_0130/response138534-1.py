
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(
        region,
        aws_access_key_id=creds['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY']
    )
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Perform deletion
    for eli in elis:
        r = eli.release()  # Assuming this does the deletion

    # Optionally, you can give feedback to the user
    flash('Elastic IP deleted successfully.')

    # Redirect back to the page with the delete button
    return redirect(url_for('your_target_route', region=region))

# Define your target route where the button is present
@app.route('/elastic_ips/<region>')
def your_target_route(region):
    # Render your template that includes the delete button
    return render_template('your_template.html', region=region)

if __name__ == '__main__':
    app.run()
