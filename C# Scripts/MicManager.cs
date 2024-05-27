using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MicManager : MonoBehaviour
{
    AudioClip record;
    AudioSource aud;

    // Start is called before the first frame update
    void Start()
    {
        aud = GetComponent<AudioSource>();
    }

    public void PlaySound()
    {
        aud.Play();
    }

    public void RecSound()
    {
        // Check the device
        foreach (var device in Microphone.devices)
        {
            Debug.Log("Mic Name: " + device);
        }

        // Recording for 3 Seconds
        record = Microphone.Start(Microphone.devices[0].ToString(), false, 3, 44100);

        // Save the audio to .wav file
        SavWav.Save("user_speak", record);
    }
}
