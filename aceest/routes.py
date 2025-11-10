from flask import jsonify, request
from .models import Gym, sessions

def register_routes(app):
    @app.get('/health')
    def health():
        return jsonify({'status': 'ok'}), 200

    @app.get('/gyms')
    def list_gyms():
        return jsonify([g.to_dict() for g in sessions.values()]), 200

    @app.post('/gyms')
    def create_gym():
        payload = request.get_json() or {}
        name = payload.get('name')
        if not name:
            return jsonify({'error': 'name required'}), 400
        g = Gym.create(name)
        return jsonify(g.to_dict()), 201

    @app.get('/gyms/<int:gym_id>')
    def get_gym(gym_id):
        g = sessions.get(gym_id)
        if not g:
            return jsonify({'error': 'not found'}), 404
        return jsonify(g.to_dict())

    @app.post('/gyms/<int:gym_id>/members')
    def add_member(gym_id):
        g = sessions.get(gym_id)
        if not g:
            return jsonify({'error': 'not found'}), 404
        payload = request.get_json() or {}
        member = payload.get('member')
        if not member:
            return jsonify({'error': 'member required'}), 400
        g.add_member(member)
        return jsonify(g.to_dict()), 200
