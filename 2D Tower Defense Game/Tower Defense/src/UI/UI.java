package UI;

import java.util.ArrayList;

import org.lwjgl.input.Mouse;
import static Helper.Translator.*;

public class UI {

	private ArrayList<Button> buttonList;
	private ArrayList<Menu> menuList;

	public UI() {
		buttonList = new ArrayList<Button>();
		menuList = new ArrayList<Menu>();

	}

	public void addButton(String name, String textureName, int x, int y) {// method that adds buttons and its textures
		buttonList.add(new Button(name, QuickLoad(textureName), x, y));
	}

	public boolean isButtonClicked(String buttonName) {
		Button b = getButton(buttonName);
		float mouseY = HEIGHT - Mouse.getY() - 1;
		if (Mouse.getX() > b.getX() && Mouse.getX() < b.getX() + b.getWidth() && mouseY > b.getY()
				&& mouseY < b.getY() + b.getHeight()) {// checking to see if mouse is on top of a button
			return true;
		}
		return false;
	}

	private Button getButton(String buttonName) {// looks through lists of button and find one with buttonname, then
													// return that button
		for (Button b : buttonList) {
			if (b.getName().equals(buttonName)) {
				return b;
			}
		}
		return null;
	}

	public void createMenu(String name, int x, int y) {
		menuList.add(new Menu(name, x, y));
	}

	public Menu getMenu(String name) {
		for (Menu m : menuList)
			if (name.equals(m.getName()))
				return m;
		return null;
	}

	public void draw() {
		for (Button b : buttonList)
			DrawQuadTex(b.getTexture(), b.getX(), b.getY(), b.getWidth(), b.getHeight());
		for (Menu m : menuList)
			m.draw();
	}

	public class Menu {
		private ArrayList<Button> menuButtons;
		private int x, y, buttonAmount;
		String name;

		public Menu(String name, int x, int y) {
			this.name = name;
			this.x = x;
			this.y = y;
			this.buttonAmount = 0;
			this.menuButtons = new ArrayList<Button>();
		}

		public void addButton(Button b) {
			b.setX(x + buttonAmount * TILE_SIZE);
			buttonAmount++;
			menuButtons.add(b);
		}

		public boolean isButtonClicked(String buttonName) {
			Button b = getButton(buttonName);
			float mouseY = HEIGHT - Mouse.getY() - 1;
			if (Mouse.getX() > b.getX() && Mouse.getX() < b.getX() + b.getWidth() && mouseY > b.getY()
					&& mouseY < b.getY() + b.getHeight()) {// checking to see if mouse is on top of a button
				return true;
			}
			return false;
		}

		private Button getButton(String buttonName) {// looks through lists of button and find one with buttonname, then
														// return that button
			for (Button b : menuButtons) {
				if (b.getName().equals(buttonName)) {
					return b;
				}
			}
			return null;
		}

		public void draw() {
			for (Button b : menuButtons)
				DrawQuadTex(b.getTexture(), b.getX(), b.getY(), b.getWidth(), b.getHeight());
		}

		public String getName() {
			return name;
		}
	}
}
