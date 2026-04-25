
from flask import Flask, redirect, url_for, flash
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Attempt to delete the IPs
    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message indicating success or failure
    flash(f'Deleted IP: {ip.decode("ascii")}', 'success')

    # Redirect back to the page where the delete button is located
    return redirect(url_for('your_view_function', region=region))

# Example of the view function that you'd redirect to
@app.route('/elastic_ips/<region>')
def your_view_function(region):
    # Your logic to show the elastic IPs
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
