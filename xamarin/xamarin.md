---
title: "Xamarin"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Xamarin
All that is left of Microsoft's mobile strategy?

[Xamarin Recipes](https://github.com/xamarin/recipes)
[Accelerometer Instructions](https://developer.xamarin.com/recipes/android/os_device_resources/accelerometer/get_accelerometer_readings/)

# Fundamentals
* Assume in the following you are using Visual Studio 2017
* For Xamarin these are docuemnted [here](https://developer.xamarin.com/recipes/android/fundamentals/intent/)
* Here is a more detailed Android (Google) take on the [matter](https://developer.android.com/guide/components/fundamentals.html)
* Activities - these are the screens in an application. You need to understand 
  * how to start one
  * how to pass data between them
* Intents - An abstract concept specifying what you want to do
  * What the intent is (like make a phone call)
  * What data does it need
* Services - A process who's lifecycle is not necessarily tied to the lifecycle of an activity

# ThingsGetting Started
* Need to install Visual Studio Xamarin extensions first (under menu Tools/Extensions and Updates)
* You start by creating a blank Xamarin app

# Important Artifacts
* Activity
  * When you create a Blank Android app you get one for free (MainActivty)
  * You create an new activity with Add Item (don't forget to give it a reasonable name)
  * You will need to start it from an event handler. For example putting this in MainActivity *OnCreate* startes it when you click on the *_infoButton*
    *        _infoButton.Click += (sender, e) =>
            {
                var intent = new Intent(this, typeof(InfoActivity));
                StartActivity(intent);
            };
  * You probably need to create a layout for it, and additionally you need this statment in your new activitie *OnCreate*
    *       SetContentView(Resource.Layout.infoLayout);
    * This *Resource.Layout.infoLayout* is defined in the Resources, but it is not in the axml file oddly enough
* Layouts
  * You get one for free with a blank Android, but a cheesy LinearLayout
  * They have the "axml" extension and are really XML manifiests
  * Best to create it after left-clicing on the *Resources/Layout* folder 
    * If you don't it seemingly breaks the project!!!
  * It has to be wired to the Activyt with *SetContentView(Resource.Layout.infoLayout)* - see above
  * When created Layouts get a Resource Layout ID created and associated with them
     * This can be seen by clicking on *Resources/Resource.Designer.cs/Resource/Layout* and inspecting the members
     * As far as I can tell it is only used in SetContentView
* TextViews
  * This is a control with which you can display textual information
  * Not clear to me how you are supposed to give it a reasonable name, but you can rename it manually:
     * Go to the *Resource.ID* code definition and use the rename function.
     * You need to change the entry in the axml file manually then, as rename will not find it there.

  * You create them by dragging them from the Toolbox window on the left into your desired Layout in Design Mode
    * When created TextViews get a Resource ID created and associated with them
     * This can be seen by clicking on *Resources/Resource.Designer.cs/Id/Layout* and inspecting the members
     

# Questions
* How am I supposed to name the TextView on drag and drop?     



# Acceleratometer changes
* Seeminingly "Activity1" is now called "MainActivity"
* had to add some namespaces
  * "using Android.Hardware;"
  * "using Android.Content;"
* Had to add an ISensorEventLister interface declatation to MainAcitivity
  * As in " public class MainActivity : Activity, ISensorEventListener"