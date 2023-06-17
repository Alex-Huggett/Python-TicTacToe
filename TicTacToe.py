class Square :

    def __init__ ( self ) :

        self . Value = 0

class Board :

    def __init__ ( self , size = 3 ) :

        self . Board : list [ list [ Square ] ] = [ 
            [ Square ( ) 
            for x in range ( size ) ] 
            for y in range ( size ) 
            ]
        
    def Move ( self , PlayerTurn , Move ) :

        PlacedOnSquare : Square = self . Board [ Move [ 1 ] ] [ Move [ 0 ] ]

        if PlacedOnSquare . Value == 0 :

            PlacedOnSquare . Value = PlayerTurn

            return ( True )
        
        else :

            return ( False )

    def Display ( self ) :

        print ( ' ' +  '_' * ( len ( self . Board ) * 2 - 1 ) )

        for y in range ( len ( self . Board ) ) :

            print ( '|' , end = '' )

            for x in range ( len ( self . Board [ y ] ) ) :

                Value = self . Board [ y ] [ x ] . Value

                print ( str ( Value ) , end = '' )

                if not x == len ( self . Board [ y ] ) - 1 :

                    print ( end = ' ' )

            print ( '|' )

        print ( ' ' +  '‾' * ( len ( self . Board ) * 2 - 1 ) )

b = Board ( )
b . Display ( )