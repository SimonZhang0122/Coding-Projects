package Data;

import static Helper.Translator.BeginSession;

import org.lwjgl.opengl.Display;

import Helper.Clock;
import Helper.StateManager;

public class Start {

	public Start() {
		// calls the beginsession method from the translator class
		BeginSession();

		// Main game loop
		while (!Display.isCloseRequested()) {
			Clock.update();
			StateManager.update();
			Display.update();// updates and save the display screen
			Display.sync(60);// sets the fps of the game
		}
		Display.destroy();// close the game
	}

	public static void main(String[] args) {
		new Start();
	}
}