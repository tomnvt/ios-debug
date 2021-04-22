//
//  ContainerBuilder.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import Swinject

class ContainterBuilder {

    static func buildContainer() -> Container {
        var container = Container()
        container = registerRepositoryLayer(to: container)
        return container
    }
    
    static func registerRepositoryLayer(to container: Container) -> Container {
        let container = Container.init(parent: container, defaultObjectScope: .container)

        container.register(AwesomeRepository.self) { _ in
            AwesomeRepositoryImpl()
        }

        return container
    }
}
