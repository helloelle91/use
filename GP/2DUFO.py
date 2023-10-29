-----------PlayerController------------------
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    private Rigidbody2D rbd;
    public float speed;
    public Text winText;
    public Text countText;
    public int count=0;
    // Start is called before the first frame update
    void Start()
    {
        rbd = GetComponent<Rigidbody2D>(); 
        //getting component by initializing
    }

    // Update is called once per frame
    void FixedUpdate() 
        //void update changed to fixedupdate
    {
        float moveHorizontal = Input.GetAxis("Horizontal"); 
        float moveVertical = Input.GetAxis("Vertical");
        Vector2 movement = new Vector2(moveHorizontal, moveVertical);
        rbd.AddForce(movement*speed);
    }
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag=="PickUp")
        {
            other.gameObject.SetActive(false);
            count++;
            SetCountText();
        }
    }
    void SetCountText()
    {
        countText.text = "Count" + count.ToString();
        if(count==7)
        {
            winText.text = "jeet gaye aap";
        }
    }
}

----------CameraController------------
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject player;
    private Vector3 offset;
    // Start is called before the first frame update
    void Start()
    {
        offset = transform.position - player.transform.position; 
    }

    // Update is called once per frame
    void LateUpdate()
    {
        transform.position = player.transform.position + offset;
    }
}
-------Rotator---------
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(0, 0, 45) * Time.deltaTime);
    }
}
