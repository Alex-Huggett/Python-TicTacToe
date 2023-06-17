class Square :

    def __init__ ( self ) :

        self . Value = 0

class Board :

    def __init__ ( self , size = 3 ) :

        self . Board : list [ list [ Square ] ] = [ 
            [ Square ( ) 
            for y in range ( size ) ] 
            for x in range ( size ) 
            ]
        
    def Move ( self , PlayerTurn , Move ) :

        PlacedOnSquare : Square = self . Board [ Move [ 0 ] ] [ Move [ 1 ] ]

        if PlacedOnSquare . Value == 0 :

            PlacedOnSquare . Value = PlayerTurn

            return ( True )
        
        else :

            return ( False )

    def Display ( self ) :

        for x in range ( len ( self . Board ) ) :

            pass