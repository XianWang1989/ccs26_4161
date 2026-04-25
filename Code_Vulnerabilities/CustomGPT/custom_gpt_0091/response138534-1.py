
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

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

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optionally flash a message to the user
    flash('Elastic IP deleted successfully')

    # Redirect back to the desired page (you can customize this URL)
    return redirect(url_for('your_target_route', region=region))

@app.route('/your_target_route/<region>')
def your_target_route(region):
    # Your code to render the page with delete button
    return f"Page for region: {region}"  # Replace with your actual rendering logic

if __name__ == '__main__':
    app.run(debug=True)
