//
//  AwesomeRepository.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import Foundation

protocol AwesomeRepository {

    func doAwesomeThings()
    func doGenericAwesomeThings<T>(type: T.Type)
    func doAwesomeThingsWithTupleParameter(tupleList [(first: String, second: String)])
    func doAwesomeThingsAndReturnSingle() -> Single<String>
}
