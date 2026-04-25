
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        result = []
        r = eli.release()  # Assuming this is successful
        result.append(r)

    # Flash a message (optional, for user feedback)
    flash(f'Successfully deleted elastic IP {ip} in region {region}.')

    # Redirect back to the desired route, e.g., a list of elastic IPs
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region=None):
    # Code for listing elastic IPs for the given region
    return render_template('elastic_ips_list.html', region=region)

# Ensure to configure your app for flashing messages if using it
app.secret_key = 'your_secret_key'

if __name__ == "__main__":
    app.run(debug=True)
