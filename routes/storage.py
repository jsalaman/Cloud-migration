from __main__ import app
import os
from flask import jsonify, request
from pkg.azure import storage as st


@app.route('/storage/create', methods=['POST'])
def storage_create():
    if request.method == 'POST':
        project  = request.get_json()['project']
        storage = request.get_json()['storage']
        container = request.get_json()['container']
        access_key = request.get_json()['access_key']
        storage_created = st.create_storage(project, storage, container, access_key)
        if storage_created:
            return jsonify({'status': '200'})
        else:
            return jsonify({'status': '500'})

@app.route('/storage/get', methods=['GET'])
def storage_get():
    if request.method == 'GET':
        name = request.args.get('name')
        return jsonify(st.get_storage(name))


@app.route('/storage/update', methods=['POST'])
def storage_update():
    if request.method == 'POST':
        project  = request.get_json()['project']
        storage = request.get_json()['storage']
        container = request.get_json()['container']
        access_key = request.get_json()['access_key']
        storage_updated = st.update_storage(project, storage, container, access_key)
        if project_updated:
            return jsonify({'status': '200'})
        else:
            return jsonify({'status': '500'})