package Data;

public class WaveManager {// manages the number, hp, speed and everything about the enemy

	private float timeSinceLastWave, timeBetweenEnemies;
	int WaveNumber, enemiesPerWave;
	private Enemy enemyType;
	private Wave currentWave;

	public WaveManager(Enemy enemyType, float timeBetweenEnemies, int enemiesPerWave) {// constructor
		this.enemyType = enemyType;
		this.enemiesPerWave = enemiesPerWave;
		this.timeBetweenEnemies = timeBetweenEnemies;
		this.timeSinceLastWave = 0;
		this.WaveNumber = 0;
		this.currentWave = null;
		newWave();
	}

	public void update() {
		if (!currentWave.isCompleted()) // check if current wave is over or not, if not keep updating and spawning
										// enemies
			currentWave.update();
		else
			newWave();// starts a new wave when current wave is over
	}

	private void newWave() {
		currentWave = new Wave(enemyType, timeBetweenEnemies, enemiesPerWave);
		WaveNumber++;
		System.out.println("Beginning Wave" + WaveNumber);
	}

	public Wave getCurrentWave() {
		return currentWave;
	}
}
