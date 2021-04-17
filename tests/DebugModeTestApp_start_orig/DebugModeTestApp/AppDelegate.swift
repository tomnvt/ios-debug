//
//  AppDelegate.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    func presentFirstScreen(application: UIApplication) {
        let localWindow = UIApplication.shared.windows.filter { $0.isKeyWindow }
            .first ?? UIWindow()

        localWindow.rootViewController = UINavigationController()
        localWindow.makeKeyAndVisible()
        window = localWindow
    }
}

