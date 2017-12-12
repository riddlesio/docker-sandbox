<?php
// __main__

namespace AIGames\PHPBot;

/**
 * Class Game
 * @package AIGames\PHPBot
 */
class Game
{

    public function __construct() {}

    /**
     * Returns the requested setting variable
     * @param $setting
     * @return null
     */
    public function get($setting)
    {
        if (array_key_exists($setting, $this->settings)) {
            return $this->settings[$setting];
        } else {
            return null;
        }
    }

    /**
     * Main Function that continuously receives STDIN input
     */
    public function run() {
        $handle = fopen("php://stdin", "r");

        while(!feof($handle)) {
            $command = trim(fgets($handle));

            if ($command == "") {
                continue;
            }

            if ($command == "exit") {
                $this->output("bye");
                break;
            }

            $this->processInput($command);
        }
        fclose($handle);
    }

    public function output($string) {
        echo $string."\n";
    }

    /**
     * Processes the command input and calls the required method.
     * Returns true if command is accepted, false if the command is unrecognized
     *
     * @param $input
     * @return bool
     */
    public function processInput($input) {
        $splitstring = explode(" ", $input);

        if ($splitstring[0] === 'settings') {
          file_put_contents("php://stderr",$input);
        }

        if ($splitstring[0] === 'update') {
          file_put_contents("php://stderr",$input);
        }

        if ($splitstring[0] === 'action') {
             $getRandInt = rand ( 0 , 2 );
             if( $getRandInt == 0 ){
                $this->output("rock");
             }
             if( $getRandInt == 1 ){
                $this->output("paper");
             }
             if( $getRandInt == 2 ){
                $this->output("scissors");
             }
        }

        return false;
    }
}

$game = new Game();
$game->run();