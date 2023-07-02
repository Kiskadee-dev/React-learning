import React, { useLayoutEffect } from 'react'
import { SafeAreaView } from 'react-native-safe-area-context';
import { Text, View, Image, TextInput, ScrollView } from 'react-native'
import { useNavigation } from "@react-navigation/native";
import { AdjustmentsVerticalIcon, ChevronDownIcon, MagnifyingGlassCircleIcon, MagnifyingGlassIcon, MagnifyingGlassPlusIcon, UserIcon } from "react-native-heroicons/outline";
import Categories from '../components/Categories';
import FeaturedRow from '../components/FeaturedRow';

const HomeScreen = () => {
    const navigation = useNavigation();
    useLayoutEffect(() => {
        navigation.setOptions({
            headerShown: false,
        });
    }, [])
    return (
        <SafeAreaView className="bg-white pt-5">
            <View className="flex-row pb-3 items-center mx-4 space-x-2">
                <Image
                    source={{
                        uri: 'https://links.papareact.com/wru'
                    }}
                    className='h-7 w-7 bg-gray-300 p-4 rounded-full'
                />
                <View className="flex-1">
                    <Text className="font-bold text-gray-400 text-xs">
                        Deliver Now!</Text>
                    <Text className="font-bold text-xl">
                        Current Location
                        <ChevronDownIcon size={20} color="#00CCBB"/>                        
                    </Text>
                </View>
                <UserIcon size={35} color="#00CCBB"></UserIcon>
            </View>

            {/* Barra de busca */}
            <View className="flex-row items-center space-x-2  pb-2 mx-4 ">
                <View className="flex-row flex-1 space-x-2 bg-gray-200 p-3">
                    <MagnifyingGlassIcon color="#00CCBB" />
                    <TextInput placeholder='Restaurants and cuisines'
                    keyboardType='default'
                    />
                </View>
                <AdjustmentsVerticalIcon color="#00CCBB" />
            </View>
            {/* content body*/}
            <ScrollView className='bg-gray-100'>
                {/* Categories */}
                <Categories/>
                {/* Featured Rows */}
                <FeaturedRow
                id="123"
                title="Featured"
                description="Paid placements from our partners"
                />
                <FeaturedRow
                id="1234"
                title="Tasty Discounts"
                description="Everyone is enjoying these discounts!"
                />
                <FeaturedRow
                id="1235"
                title="Offers near you!"
                description="Why not support your local restaurant tonight!"
                />
            </ScrollView>
        </SafeAreaView>
    )
}

export default HomeScreen
