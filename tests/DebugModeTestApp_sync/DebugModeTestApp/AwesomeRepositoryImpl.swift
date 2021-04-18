//
//  AwesomeRepositoryImpl.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import Foundation

class AwesomeRepositoryImpl {

}

// MARK: - Protocol conformance
extension AwesomeRepositoryImpl: AwesomeRepository {

    func doAwesomeThings() {
        print("Doing awesome things")
    }
}

// MARK: - Mock implementation
protocol MockAwesomeRepository: AwesomeRepository {}

class MockAwesomeRepositoryImpl: AwesomeRepository {

    private let originalInstance: AwesomeRepository

    init(originalInstance: AwesomeRepository) {
        self.originalInstance = originalInstance
    }
}

extension MockAwesomeRepositoryImpl {

    
    func doAwesomeThings() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThings()
    }

}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}

// MARK: - Mock implementation
protocol MockAwesomeRepository: AwesomeRepository {}

class MockAwesomeRepositoryImpl: AwesomeRepository {

    private let originalInstance: AwesomeRepository

    init(originalInstance: AwesomeRepository) {
        self.originalInstance = originalInstance
    }
}

extension MockAwesomeRepositoryImpl {

    
    func doAwesomeThings() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThings()
    }

}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}

// MARK: - Mock implementation
protocol MockAwesomeRepository: AwesomeRepository {}

class MockAwesomeRepositoryImpl: AwesomeRepository {

    private let originalInstance: AwesomeRepository

    init(originalInstance: AwesomeRepository) {
        self.originalInstance = originalInstance
    }
}

extension MockAwesomeRepositoryImpl {

    
    func doAwesomeThings() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThings()
    }

}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}

// MARK: - Mock implementation
protocol MockAwesomeRepository: AwesomeRepository {}

class MockAwesomeRepositoryImpl: AwesomeRepository {

    private let originalInstance: AwesomeRepository

    init(originalInstance: AwesomeRepository) {
        self.originalInstance = originalInstance
    }
}

extension MockAwesomeRepositoryImpl {

    
    func doAwesomeThings() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThings()
    }

}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}
