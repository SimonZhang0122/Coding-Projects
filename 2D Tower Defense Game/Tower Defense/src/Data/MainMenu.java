package Data;

import org.lwjgl.input.Mouse;
import org.newdawn.slick.opengl.Texture;

import Helper.StateManager;
import Helper.StateManager.GameState;
import UI.UI;

import static Helper.Translator.*;

public class MainMenu {

	private Texture background;
	private UI menuUI;

	public MainMenu() {
		background = QuickLoad("MainMenu texture");// loads the mainmenu texture to the background when game starts
		menuUI = new UI();
		menuUI.addButton("Play", "PlayButton texture", WIDTH / 2 - 128, (int) (HEIGHT * 0.70f));// adds a play button to
																								// the middle of the
																								// screen
		menuUI.addButton("Editor", "EditorButton texture", WIDTH / 2 - 556, (int) (HEIGHT * 0.70f));// adds a editor
																									// button to left of
																									// the screen
		menuUI.addButton("Quit", "QuitButton texture", WIDTH / 2 + 300, (int) (HEIGHT * 0.70f));// adds a quit button to
																								// the right of the
																								// screen
	}

	private void updateButtons() {// functions of different buttons
		if (Mouse.isButtonDown(0)) {
			if (menuUI.isButtonClicked("Play"))// when play button is clicked, start game
				StateManager.setState(GameState.GAME);
			if (menuUI.isButtonClicked(("Editor")))// when editor button is clicked, open editor mode to edit map
				StateManager.setState(GameState.EDITOR);
			if (menuUI.isButtonClicked("Quit"))// when quit button is clicked, game shuts down
				System.exit(0);
		}
	}

	public void update() {
		DrawQuadTex(background, 0, 0, 2048, 1024);
		menuUI.draw();
		updateButtons();
	}
}