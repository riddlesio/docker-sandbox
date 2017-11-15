"use strict"

/**
 * Rock Paper Scissors JavaScript bot
 *
 * Last update: June 17, 2016
 *
 * @author Niko van Meurs
 * @version 1.0
 * @License MIT License (http://opensource.org/Licenses/MIT)
 */
const createInterface = require('readline').createInterface;
const in$ = process.stdin;
const out$ = process.stdout;

class Bot {

    handleClose() {
        process.exit(0);
    }

    handleLine(data) {

        if (!data.length) {
            return;
        }

        const lines = data.trim().split('\n');

        while (lines.length) {

            const line = lines.shift().trim();
            const parts = line.split(' ');

            switch(parts[0]) {

                case 'action':
                    const possibleResponses = ['rock', 'paper', 'scissors'];
                    const random = Math.floor(Math.random() * possibleResponses.length);
                    this.out(`${possibleResponses[random]}`);
                    break;
                case 'settings':
                    process.stderr.write(parts[0] + '\n');
                    break;
                case 'update':
                    process.stderr.write(parts[0] + '\n');
                    break;
                default:
                    this.out(line);
            }
        }
    }

    out(message) {
        out$.write(`${message}\n`);
    }

    run() {
        this.io = createInterface(in$, out$);
        this.io.on('line', this.handleLine.bind(this));
        this.io.on('close', this.handleClose)
    }
}

const bot = new Bot();
bot.run();
