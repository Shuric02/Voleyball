from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Web_admins(models.Model):
    login_admin = models.CharField('login_admin', max_length=20)
    password_admin = models.CharField('password_admin', max_length=20)

    def __str__(self):
        return self.login_admin

    class Meta:
        verbose_name = 'Адміністратори'
        verbose_name_plural = 'Адміністратори'

class Players(models.Model):
    FirstName = models.CharField('FirstName', max_length= 20)
    SecondName = models.CharField('SecondName', max_length= 20)
    serve = models.IntegerField('serve', validators=[MinValueValidator(0), MaxValueValidator(5)])
    attack = models.IntegerField('attack', validators=[MinValueValidator(0), MaxValueValidator(5)])
    keep_ball = models.IntegerField('keep_ball', validators=[MinValueValidator(0), MaxValueValidator(5)])
    comand_game = models.IntegerField('comand_game', validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.SecondName

    class Meta:
        verbose_name = 'Гравці'
        verbose_name_plural = 'Гравці'


class СoefficientsOfCharacteristics(models.Model):
    serve_coef = models.FloatField('serve', validators=[MinValueValidator(0), MaxValueValidator(1)])
    attack_coef = models.FloatField('attack', validators=[MinValueValidator(0), MaxValueValidator(1)])
    keep_ball_coef = models.FloatField('keep_ball', validators=[MinValueValidator(0), MaxValueValidator(1)])
    team_game_coef = models.FloatField('team_game', validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f"Serve: {self.serve_coef}, Attack: {self.attack_coef}, Keep Ball: {self.keep_ball_coef}, Team Game: {self.team_game_coef}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Players)

    def __str__(self):
        return self.name

class MatchHistory(models.Model):
    date = models.DateField()
    teams = models.ManyToManyField(Team, through='MatchTeam')

    def __str__(self):
        team_names = ", ".join([team.name for team in self.teams.all()])
        return f"Match on {self.date}: {team_names}"

class MatchTeam(models.Model):
    match = models.ForeignKey(MatchHistory, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.team.name} in {self.match.date}"