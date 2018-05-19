/** map from controller button name to inReg bit */
const buttonMap = {
    a: 0x80,
    b: 0x40,
    select: 0x20,
    start: 0x10,
    up: 0x08,
    down: 0x04,
    left: 0x02,
    right: 0x01,
};

/** map from standard gamepad button index to inReg bit */
const gamepadMap = {
    0: buttonMap.a,
    1: buttonMap.b,
    8: buttonMap.select,
    9: buttonMap.start,
    12: buttonMap.up,
    13: buttonMap.down,
    14: buttonMap.left,
    15: buttonMap.right,
};

/** Gamepad device */
export class Gamepad {
    /** Create a Gamepad
     * @param {Gigatron} cpu - The cpu to control
     * @param {Object.<string,string[]>} keys - Map from controller button
     *  name to list of keys
     */
    constructor(cpu, keys) {
        this.cpu = cpu;
        this.pressed = 0;
        this.keyMap = {};

        /* build map from keyboard key to controller button name */
        for (let button of Object.keys(keys)) {
            for (let key of keys[button]) {
                this.keyMap[key] = buttonMap[button];
            }
        }
    }

    /** start handling key events */
    start() {
        $(document)
            .on('keydown', (event) => {
                let bit = this.keyMap[event.key];
                if (bit) {
                    this.pressed |= bit;
                    event.preventDefault();
                }
            })
            .on('keyup', (event) => {
                let bit = this.keyMap[event.key];
                if (bit) {
                    this.pressed &= ~bit;
                    event.preventDefault();
                }
            });
    }

    /** stop handling key events */
    stop() {
        $(document).off('keydown keyup');
    }

    /** check gamepads */
    tick() {
        let pressed = this.pressed;

        if (navigator.getGamepads) {
            let gamepads = navigator.getGamepads();
            for (let gamepad of gamepads) {
                if (gamepad) {
                    for (let buttonIndex of Object.keys(gamepadMap)) {
                        let bit = gamepadMap[buttonIndex];
                        if (gamepad.buttons[buttonIndex].pressed) {
                            pressed |= bit;
                        }
                    }
                }
            }
        }

        this.cpu.inReg = pressed ^ 0xff; // active low
    }
}
