from flask import Blueprint, request, jsonify
from models.player import Player
from config.database import db
# from controllers.playersController import get_players, create_player

players_bp = Blueprint('players', __name__)

# Define routes with trailing slash handling
@players_bp.route('/', methods=['GET'], strict_slashes=False)
def get_players():
    try:
        players = Player.query.all()
        return jsonify([player.serialize() for player in players])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@players_bp.route('/', methods=['POST'], strict_slashes=False)
def create_player():
    data = request.json
    try:
        player = Player(firstName=data['firstName'], lastName=data['lastName'], position=data['position'])
        db.session.add(player)
        db.session.commit()
        return jsonify(player.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# players_bp.route('', methods=['GET'])(get_players)
# players_bp.route('', methods=['POST'])(create_player)

