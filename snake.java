import javax.media.j3d.*;
import javax.vecmath.*;
import com.sun.j3d.utils.geometry.Sphere;
import com.sun.j3d.utils.universe.SimpleUniverse;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Random;

public class Snake3DGame extends JFrame implements KeyListener {
    private TransformGroup snakeTransform;
    private Vector3f snakeDirection = new Vector3f(0.1f, 0, 0);
    private ArrayList<Vector3f> snakePositions = new ArrayList<>();
    private int snakeLength = 5;
    private Random rand = new Random();
    private Vector3f foodPosition;
    
    public Snake3DGame() {
        // Setup 3D environment
        Canvas3D canvas = new Canvas3D(SimpleUniverse.getPreferredConfiguration());
        SimpleUniverse universe = new SimpleUniverse(canvas);
        BranchGroup group = new BranchGroup();

        // Create Snake
        snakeTransform = new TransformGroup();
        snakeTransform.setCapability(TransformGroup.ALLOW_TRANSFORM_WRITE);
        group.addChild(snakeTransform);

        Sphere snake = new Sphere(0.05f);
        snakeTransform.addChild(snake);

        // Create Food
        foodPosition = new Vector3f(rand.nextFloat(), rand.nextFloat(), rand.nextFloat());
        Sphere food = new Sphere(0.05f);
        TransformGroup foodTransform = new TransformGroup();
        Transform3D foodTrans = new Transform3D();
        foodTrans.setTranslation(foodPosition);
        foodTransform.setTransform(foodTrans);
        foodTransform.addChild(food);
        group.addChild(foodTransform);

        // Setup Viewing Platform
        universe.getViewingPlatform().setNominalViewingTransform();
        universe.addBranchGraph(group);

        // Window setup
        add(canvas);
        setSize(800, 600);
        setVisible(true);
        addKeyListener(this);
        
        // Initialize snake positions
        for (int i = 0; i < snakeLength; i++) {
            snakePositions.add(new Vector3f(i * -0.1f, 0, 0));
        }
    }

    public void keyPressed(KeyEvent e) {
        // Update snake direction based on key press
        switch (e.getKeyCode()) {
            case KeyEvent.VK_UP:    snakeDirection.set(0, 0.1f, 0); break;
            case KeyEvent.VK_DOWN:  snakeDirection.set(0, -0.1f, 0); break;
            case KeyEvent.VK_LEFT:  snakeDirection.set(-0.1f, 0, 0); break;
            case KeyEvent.VK_RIGHT: snakeDirection.set(0.1f, 0, 0); break;
        }
    }

    public void keyReleased(KeyEvent e) { }
    public void keyTyped(KeyEvent e) { }

    public static void main(String[] args) {
        new Snake3DGame();
    }
}
