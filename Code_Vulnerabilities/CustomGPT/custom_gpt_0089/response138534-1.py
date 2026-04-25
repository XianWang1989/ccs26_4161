
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

    try:
        for eli in elis:
            r = eli.release()  # Release the elastic IP

        flash('Elastic IP deleted successfully!', 'success')  # Flash a success message
    except Exception as e:
        flash('Error deleting Elastic IP: {}'.format(str(e)), 'danger')  # Flash an error message

    # Redirect back to the page with the delete button
    return redirect(url_for('your_view_function_name', region=region))

# Add your view function for the main page with the delete button
@app.route('/elastic_ips/<region>')
def your_view_function_name(region):
    # Render your page showing the list of elastic IPs with delete buttons
    # return render_template('your_template.html', region=region)
