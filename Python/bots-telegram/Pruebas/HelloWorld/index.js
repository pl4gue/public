'use strict';

const Telegraf = require('telegraf');



const Token = '328909176:AAF77tqnYzyLEV5pYfyXi1QMM7EhkqDINIk';
const app = new Telegraf(Token);



app.command('hello', (ctx) => ctx.reply('Hola!!'))
app.hears('ieee', (ctx) => ctx.reply('ieee'))


app.catch((err) => {
    console.log('[ERROR] - ', err)
})

app.startPolling()
