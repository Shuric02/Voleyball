from django.shortcuts import render, redirect, get_object_or_404
from .models import Web_admins, Players, СoefficientsOfCharacteristics, MatchHistory, MatchTeam, Team


def about_us(request):
    return render(request, 'about-us.html')

def autorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Web_admins.objects.get(login_admin=username, password_admin=password)
            return redirect('main_page')
        except Web_admins.DoesNotExist:
            error_message = 'Невірний логін або пароль'
            return render(request, 'Autorization.html', {'error_message': error_message})
    return render(request, 'Autorization.html')

def main_page(request):
    players = Players.objects.all()
    return render(request, 'MainPage.html', {'players': players})

def registrationPlayers(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        serve = request.POST.get('serve')
        attack = request.POST.get('attack')
        keep_ball = request.POST.get('keep_ball')
        comand_game = request.POST.get('comand_game')

        Players.objects.create(
            FirstName=first_name,
            SecondName=second_name,
            serve=serve,
            attack=attack,
            keep_ball=keep_ball,
            comand_game=comand_game
        )
        return redirect('main_page')

    return render(request, 'registrationPlayers.html')

def edit_player(request, player_id):
    player = get_object_or_404(Players, id=player_id)

    if request.method == 'POST':
        player.FirstName = request.POST.get('first_name')
        player.SecondName = request.POST.get('second_name')
        player.serve = request.POST.get('serve')
        player.attack = request.POST.get('attack')
        player.keep_ball = request.POST.get('keep_ball')
        player.comand_game = request.POST.get('comand_game')
        player.save()
        return redirect('main_page')

    return render(request, 'edit_player.html', {'player': player})

def delete_player(request, player_id):
    player = get_object_or_404(Players, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('main_page')

    return render(request, 'delete_confirmation.html', {'player': player})

def edit_coefficient(request, id):
    coef = get_object_or_404(СoefficientsOfCharacteristics, id=id)
    if request.method == 'POST':
        coef.serve_coef = request.POST.get('serve_coef')
        coef.attack_coef = request.POST.get('attack_coef')
        coef.keep_ball_coef = request.POST.get('keep_ball_coef')
        coef.team_game_coef = request.POST.get('team_game_coef')
        coef.save()
        return redirect('edit_coefficient', id=coef.id)
    return render(request, 'edit_coefficient.html', {'coef': coef})


def select_players(request):
    players = Players.objects.all()
    return render(request, 'SortPlayers.html', {'players': players})


def sort_players(request):
    if request.method == 'POST':
        selected_player_ids = request.POST.getlist('selected_players')
        selected_players = Players.objects.filter(id__in=selected_player_ids)

        coefficients = СoefficientsOfCharacteristics.objects.first()

        players_with_scores = []
        for player in selected_players:
            total_score = (
                    player.serve * coefficients.serve_coef +
                    player.attack * coefficients.attack_coef +
                    player.keep_ball * coefficients.keep_ball_coef +
                    player.comand_game * coefficients.team_game_coef
            )
            players_with_scores.append({
                'player': player,
                'total_score': total_score
            })

        num_players = len(players_with_scores)
        if num_players <= 12:
            num_teams = 2
        elif 12 < num_players <= 18:
            num_teams = 3
        else:
            num_teams = num_players // 6

        players_with_scores.sort(key=lambda x: x['total_score'], reverse=True)

        teams = [[] for _ in range(num_teams)]
        team_scores = [0] * num_teams

        for player_data in players_with_scores:
            min_team_index = team_scores.index(min(team_scores))
            teams[min_team_index].append(player_data)
            team_scores[min_team_index] += player_data['total_score']

        context = {
            'teams': teams,
        }

        from datetime import date
        match_history = MatchHistory.objects.create(date=date.today())

        for index, team_players in enumerate(teams):
            team = Team.objects.create(name=f"Команда {index + 1}")
            for player_data in team_players:
                team.players.add(player_data['player'])
            team.save()

            MatchTeam.objects.create(match=match_history, team=team)

        return render(request, 'sort_players.html', context)

    return render(request, 'SortPlayers.html', {'players': Players.objects.all()})

def match_history(request):
    matches = MatchHistory.objects.prefetch_related('teams').order_by('-id')
    context = {
        'matches': matches
    }
    return render(request, 'history.html', context)
