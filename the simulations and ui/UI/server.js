const express = require('express');
const path = require('path');
const { exec } = require("child_process");
const bodyParser = require('body-parser');
const app = express();
const fs = require('fs');
const directoryPath = path.join('..\\inverse_tug_of_war\\', 'controllers');
const scoresPath = path.join('public\\', 'gamescores.txt');
const tournamentPath = path.join('public\\', 'tournament.txt');

var tournamentPoint = 0;

app.use('/static', express.static('public'))
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.engine('html', require('ejs').renderFile);

app.get('/information', function(req, res) {
  res.sendFile(path.join(__dirname, '/information.html'));
});

function getControllers (next){
    console.log('fetching controllers');
    var allControllers = [];

    fs.readdir(directoryPath, function (err, files) {
        //handling error
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        }
        //listing all folders using forEach
        files.forEach(function (file) {
            if (!(file.includes('supervisor'))){
              if (!(file.includes('template'))){
                allControllers.push(file);
              }
            }
        });
        console.log(typeof allControllers);
        next(allControllers);
      });
    }

function getScores (next){
  fs.readFile(scoresPath, 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    data = data.replace(/\r?\n|\r/g, " ");
    console.log(data);
    next(data);
  });
}

function getTournament (next){
  fs.readFile(tournamentPath, 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    data = data.replace(/\r?\n|\r/g, " ");
    console.log(data);
    next(data);
  });
}

function prepareWorld (worldName, controller1, controller2){
  console.log("name of simulation is " + worldName + " controller1 " + controller1  + " controller2 " + controller2);
  var fs = require('fs')
  fs.readFile("..\\inverse_tug_of_war\\worlds\\templates\\"  + worldName +"_template.wbt", 'utf8', function (err,data) {
      if (err) {
          return console.log(err);
      }
      var result1 = data.replace('empty_robot1', controller1);
      var result2 = result1.replace('empty_robot2', controller2);

      fs.writeFile("..\\inverse_tug_of_war\\worlds\\"  + worldName + ".wbt", result2, 'utf8', function (err) {
          if (err) return console.log(err);
      });
  });
}

function prepareWorldTournament (worldName, controller1, controller2){
  console.log("name of simulation is " + worldName + " controller1 " + controller1  + " controller2 " + controller2);
  var fs = require('fs')
  fs.readFile("..\\inverse_tug_of_war\\worlds\\templates\\"  + worldName +"_template_t.wbt", 'utf8', function (err,data) {
      if (err) {
          return console.log(err);
      }
      var result1 = data.replace('empty_robot1', controller1);
      var result2 = result1.replace('empty_robot2', controller2);

      fs.writeFile("..\\inverse_tug_of_war\\worlds\\"  + worldName + ".wbt", result2, 'utf8', function (err) {
          if (err) return console.log(err);
      });
  });
}

app.get('/main', function(req, res) {
    getControllers(function (controllers) {
        getScores(function (scores) {
            getTournament(function (tournament) {
                console.log("atttempt render");
                res.render(__dirname + "/testdisplay.html", {controllers:controllers, scores:scores, tournament:tournament});
            });
        });
    });
});

app.post('/single-simulation', function(req, res) {
    prepareWorld(req.body.name, req.body.controller1, req.body.controller2);

    exec("webots --stdout --fullscreen ..\\inverse_tug_of_war\\worlds\\" + req.body.name + ".wbt", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return res.redirect('/main');
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return res.redirect('/main');
        }
        console.log(`stdout: ${stdout}`);
        return res.redirect('/main');
    });
});

app.post('/tournament', function(req, res) {
      prepareWorldTournament("tugofwar", req.body.TugOfWar1, req.body.TugOfWar2);
      prepareWorldTournament("robosumo", req.body.RoboSumo1, req.body.RoboSumo2);
      prepareWorldTournament("dragrace", req.body.DragRace1, req.body.DragRace2);
      prepareWorldTournament("cagefight", req.body.CageFight1, req.body.CageFight2);

      exec("webots --stdout --fullscreen ..\\inverse_tug_of_war\\worlds\\tugofwar.wbt", (error, stdout, stderr) => {
          if (error) {
              console.log(`error: ${error.message}`);
          }
          if (stderr) {
              console.log(`stderr: ${stderr}`);
          }
          console.log(`stdout: ${stdout}`);
          exec("webots --stdout --fullscreen ..\\inverse_tug_of_war\\worlds\\robosumo.wbt", (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
            }
            console.log(`stdout: ${stdout}`);
            exec("webots --stdout --fullscreen ..\\inverse_tug_of_war\\worlds\\dragrace.wbt", (error, stdout, stderr) => {
              if (error) {
                  console.log(`error: ${error.message}`);
              }
              if (stderr) {
                  console.log(`stderr: ${stderr}`);
              }
              console.log(`stdout: ${stdout}`);
              exec("webots --stdout --fullscreen ..\\inverse_tug_of_war\\worlds\\cagefight.wbt", (error, stdout, stderr) => {
                if (error) {
                    console.log(`error: ${error.message}`);
                    return res.redirect('/main');
                }
                if (stderr) {
                    console.log(`stderr: ${stderr}`);
                    return res.redirect('/main');
                }
                console.log(`stdout: ${stdout}`);
                return res.redirect('/main');
              });
            });
          });
      });
});




app.post('/add', function(req,res){
    console.log(req.body.name);
    return res.redirect('/');
});





app.listen(8080);
