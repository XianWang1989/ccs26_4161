
from flask import Flask, flash, redirect, url_for

# After the deletion:
flash('Elastic IP has been successfully deleted.')
return redirect(url_for('list_elastic_ips', region=region))
